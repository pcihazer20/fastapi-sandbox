import json


class Note:
    def __init__(self,title:str, content:str, author:str):
        self.title = title
        self.content = content
        self.author = author


if __name__ == '__main__':

    note = Note(title="Boxing Business Brainstorm",content='', author="Rafa")
    print(note.title)
    print(note.content)
    print(note.author)

