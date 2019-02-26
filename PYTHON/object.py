class HTMLform:
    def __init__(self, name, method, action):
        self.fields = []
        self.name = name
        self.method = method
        self.action = action

    def add_field(self, label, type, min_width):
        if type not in ["text", "passweor", "email", "checkbox", "radiobutton", "textarea"]:
            raise ValueError("Type is not allowed:" + type)
        field = {"label" : label,
                 "type" : type,
                 "min_width" : min_width}
        self.field.append(field)

    def show(self): #print
        print("==={}===".format(self.name))
        print("<form method='{}' action='{}'>".format(self.method, self.action))
        for field in self.fields:
            if field["type"] == "text":
                print("{}: <input type=""text"" name=""value"" />".format(field["label"])
            elif field["type"] == "password":
                print("{}: <input type=""password"" name=""value"" />".format(field["label"])#kkas nav
            elif field["type"] == "email":
                print("{}: <input type=""email"" name=""value"" />".format(field["label"])# kkas nav
        print("</form>")


kontaktforma = HTMLform(name="Kontaktforma", method="POST", action="/contactform/submit")
kontaktforma.add_field(label="Vārds", type="email", min_width=6)
kontaktforma.add_field(label="Telefons", type="text", min_width=9)

kontaktforma.show()







