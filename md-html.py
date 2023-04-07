from markdown import markdown

text = ""
filename = input("Filename of markdown file (without .md): ")
with open(f"{filename}.md", 'r') as f:
    text = f.read()

md = markdown(text)
print(md)