# Writing in .docx

### Select doc

---

`pip install python-docx`

``` os.chdir(os.path.join(settings.BASE_DIR, 'contract_docs'))```

```doc = docx.Document("tas.docx") ```

### Select table & write in cell

---

for first table

```doc.tables[0].cell(0, 0).text = "Your_TEXT"  ```

### Convert .docx to pdf

`import win32com.client as client`

`filepath = os.path.join(settings.BASE_DIR, 'contract_docs\\tass.docx')`

`try:`

​      `word = client.DispatchEx("Word.Application")`

​      `target_path = filepath.replace(".docx", r".pdf")`

​      `word_doc = word.Documents.Open(filepath)`

​      `word_doc.SaveAs(target_path, FileFormat=17)`

​      `word_doc.Close()`

`except Exception as e:`

​        `raise e`

`finally:`

​       ` word.Quit()`













