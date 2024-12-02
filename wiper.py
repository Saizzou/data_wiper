import os
import sys, ctypes
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QTextCursor
from main_ui import Ui_Dialog  # Replace with your actual UI module
from splash_ui import Ui_MainWindow


app = QApplication(sys.argv)
mainWindow = QWidget()
splash = QWidget()
main_ui = Ui_Dialog()
splash_ui = Ui_MainWindow()
main_ui.setupUi(mainWindow)


def is_admin():
    """
    Überprüfe ob die App als Admin ausgeführt wurden ist. Ohne Admin Rechte können möglicherweise 
    nicht alle Daten gelöscht werden.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{sys.argv[0]}"', None, 1
    )
    sys.exit()


def show_splash_and_main():
    """
    Zeigt erst ein Splash Screen und nachträglich die Main App.
    """
    splash_ui.setupUi(splash)
    splash.show()
    splash.repaint()
    app.processEvents()

    QTimer.singleShot(3000, splash.close)
    QTimer.singleShot(3000, mainWindow.show)


def get_free_space_bytes(drive_path):
    """
    Zeigt dem Freien Speicher an. 
    
    Args:
        drive_path (str): Pfad zum Datenträger.
    """
    if os.name == 'nt':  # Windows
        import ctypes
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive_path, None, None, ctypes.pointer(free_bytes))
        return free_bytes.value
    else:  # Unix/Linux
        statvfs = os.statvfs(drive_path)
        return statvfs.f_bavail * statvfs.f_frsize


def update_last_line(plain_text_edit, new_text):
    """
    Eine extra funktion damit die letzte linie besser angezeigt wird.
    """
    cursor = plain_text_edit.textCursor()
    cursor.movePosition(QTextCursor.End)
    cursor.select(QTextCursor.BlockUnderCursor)
    cursor.removeSelectedText()
    cursor.insertText(new_text)
    plain_text_edit.setTextCursor(cursor)


def write_random_data(drive_path, buffer_size=64 * 1024):
    """
    Schreibt random Daten auf dem Datenträger. Dies ist nötig um alte gelöschte Daten zu überschreiben.
    """
    try:
        free_space = get_free_space_bytes(drive_path)
        if free_space == 0:
            main_ui.text_Status.appendPlainText("Datenträger ist bereits Voll!")
            return

        main_ui.text_Status.appendPlainText(f"Startet mit der Auffüllung: {drive_path}")
        main_ui.text_Status.appendPlainText(f"Freier Speicherplatz: {free_space / (1024 * 1024):.2f} MB")


        file_counter = 0
        while free_space > 0:
            file_name = os.path.join(drive_path, f"random_data_{file_counter}.bin")
            with open(file_name, "wb") as file:
                while free_space > 0:
                    data = os.urandom(min(buffer_size, free_space))
                    file.write(data)
                    free_space -= len(data)
                    main_ui.text_Status.moveCursor(main_ui.text_Status.textCursor().MoveOperation.End)
                    msg = f"Verbleibende Daten: {free_space / (1024 * 1024):.2f} MB"
                    update_last_line(main_ui.text_Status, msg)
                    QApplication.processEvents()
                file.flush()
            file_counter += 1
            main_ui.text_Status.appendPlainText("Datenträger wurde mit Fake Daten aufgefüllt.")

    except FileNotFoundError:
        main_ui.text_Status.appendPlainText(f"Fehler: USB Disk {drive_path} wurde nicht gefunden.")

    except PermissionError:
        main_ui.text_Status.appendPlainText("Fehler: Keine Rechte! Startet die APP mit Administrator Privilegen.")

    except Exception as e:
        main_ui.text_Status.appendPlainText(f"Ein Fehler ist aufgetreten: {e}")


def delete_all_contents(folder_path):
    """
    Löscht alle Daten die sich auf dem Datenträger befinden.
    
    Args:
        folder_path (str): Pfad zum Datenträger.
    """
    if os.path.exists(folder_path):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    main_ui.text_Status.appendPlainText(f"Daten gelöscht: {file_path}")
                except Exception as e:
                    main_ui.text_Status.appendPlainText(f"Fehler bei Löschen von: {file_path}: {e}")
            

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    os.rmdir(dir_path)  # Remove empty directory
                    main_ui.text_Status.appendPlainText(f"Daten gelöscht von: {dir_path}")
                except Exception as e:
                    main_ui.text_Status.appendPlainText(f"Fehler beim Löschen {dir_path}: {e}")

    else:
        main_ui.text_Status.appendPlainText(f"Datenträger '{folder_path}' existiert nicht.")


def wipe_usb(drive_letter):
    """
    Starter Funktion für die Ausführung. 

    Args:
        drive_letter (str): Pfad zum Datenträger.
    """
    drive_path = main_ui.line_Auswahl.text()
    print(drive_path)

    soru = QMessageBox.question(
        mainWindow,
        "Sind Sie sicher?",
        f"Warnung: Dies wird alle Daten auf {drive_letter} löschen. Drücke 'Ja' wenn du sicher bist:",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,)

    if soru != QMessageBox.Yes:
        main_ui.text_Status.appendPlainText("Vorgang wurde abgebrochen.")
        return

    try:
        main_ui.text_Status.appendPlainText("Datenträger wird mit Fake Daten ausgetauscht!")
        main_ui.text_Status.appendPlainText("Nach dem der Datenträger mit Fake Daten ausgetauscht wurde\
                                             wird der Datenträger mit weitere Fake Daten aufgefüllt.")
        main_ui.text_Status.appendPlainText("Anschliessend werden alle Daten gelöscht.")

        for root, dirs, files in os.walk(drive_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb+') as f:
                    f.write(os.urandom(os.path.getsize(drive_path)))

            main_ui.text_Status.appendPlainText("USB Daten wurde mit Fake Daten ausgetauscht.")
            main_ui.text_Status.appendPlainText("Datenträger wird mit Fake Daten aufgefüllt!")

        write_random_data(drive_path)
        delete_all_contents(drive_path)

    except FileNotFoundError:
        main_ui.text_Status.setPlainText(f"Fehler: USB Disk {drive_letter} wurde nicht gefunden.")

    except PermissionError:
        main_ui.text_Status.setPlainText("Fehler: Keine Rechte! Startet die APP mit Administrator Privilegen.")

    except Exception as e:
        main_ui.text_Status.setPlainText(f"Ein Fehler ist aufgetreten: {e}")


def select_directory():
    directory = QFileDialog.getExistingDirectory(mainWindow, "FLASH AUSWÄHLEN")
    return directory


def insert_directory_from():
    directory_path = select_directory()
    main_ui.line_Auswahl.setText(directory_path)
    main_ui.text_Status.appendPlainText(f"USB FLASH wurde ausgewählt: >>> '{directory_path}'")


def exit_app():
    sys.exit(app.exec())


main_ui.btn_Auswahl.clicked.connect(insert_directory_from)
main_ui.btn_exit.clicked.connect(exit_app)
main_ui.btn_Loeschen.clicked.connect(wipe_usb)
show_splash_and_main()
sys.exit(app.exec())