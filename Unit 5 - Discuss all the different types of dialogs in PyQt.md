<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

### Types of Dialogs in PyQt

PyQt provides several dialog types to interact with users and handle specific tasks in graphical applications. Dialogs can be **modal** (blocking the parent window until closed) or **modeless** (parent can still be accessed). Dialogs are typically built using the `QDialog` class, and PyQt offers a number of **preconfigured dialogs** for common needs.

***

## 1. **Message Dialogs** (`QMessageBox`)

Used to display information, warnings, ask questions, or report errors. Button choices and icons indicate the dialog's purpose.

**Variants:**

- Information (`QMessageBox.information`)
- Warning (`QMessageBox.warning`)
- Critical/Error (`QMessageBox.critical`)
- Question (`QMessageBox.question`)
- About (`QMessageBox.about`)

**Example:**

```python
result = QMessageBox.question(
    parent, "Question", "Continue?",
    QMessageBox.Yes | QMessageBox.No
)
```


***
## 2. **Custom Dialogs**

Define unique layouts with any widgets using `QDialog`. Customize logic, fields, or appearance.

**Example:**

```python
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello!")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Proceed with operation?"))
        layout.addWidget(buttonBox)
        self.setLayout(layout)
```


***
## 3. **Input Dialogs** (`QInputDialog`)

Prompt users for a single value, such as a string, integer, or item selection.

**Example:**

```python
text, ok = QInputDialog.getText(parent, "Input", "Enter your name:")
```


***
## 4. **File Dialogs** (`QFileDialog`)

Allow users to select files or directories from the file system.

**Example:**

```python
filename, _ = QFileDialog.getOpenFileName(parent, "Open File")
```


***
## 5. **Font Dialogs** (`QFontDialog`)

Let users choose fonts.

**Example:**

```python
font, ok = QFontDialog.getFont()
```


***
## 6. **Color Dialogs** (`QColorDialog`)

Allow color selection.

**Example:**

```python
color = QColorDialog.getColor()
```


***
## 7. **Progress Dialogs** (`QProgressDialog`)

Display the progress of lengthy operations, with optional cancellation.

**Example:**

```python
progress = QProgressDialog("Working...", "Cancel", minimum, maximum)
progress.setValue(value)
```


***
## 8. **Print Dialogs** (`QPrintDialog`)

Configure printing settings and select printers.

**Example:**

```python
printerDialog = QPrintDialog(printer, parent)
```


***
## 9. **Other Dialogs**

- **About Dialogs:** Show information about the application.
- **Wizard Dialogs:** Guide users through multi-step processes with `QWizard`.


## Summary Table

| Dialog Type | Purpose | Example Class |
| :-- | :-- | :-- |
| Message | Info, warning, question | QMessageBox |
| Custom Layout | User-defined | QDialog |
| Input | Get user input | QInputDialog |
| File/Directory | Select files/folders | QFileDialog |
| Font/Color | Choose font or color | QFontDialog, QColorDialog |
| Progress | Show operation progress | QProgressDialog |
| Print | Printing options | QPrintDialog |


***
**In PyQt, dialogs are vital for providing feedback, getting user data, and managing application flow.** You can use built-in dialogs for speed or create custom dialogs to fit any specialized need.
