from utils import get_now


class Note:
    def __init__(self, text=None):
        self.text = text
        self.dt = get_now()
        self.id = 0
        self.deleted = False
        self.saved = True

    def __repr__(self):
        return f"#{self.id}. {self.dt}, {self.text}, {self.deleted}"

    def __str__(self):
        return f'{"[*]" if self.saved==False else ""}{self.id}. {self.dt}, {self.text}'

    def print_detail(self):
        print(f"Id: {self.id}\nDate: {self.dt}\n{self.text}")

    def __setstate__(self, state):
        new_fields = {"deleted": False, "saved": True}
        for k, v in new_fields.items():
            try:
                state[k]
            except:
                state[k] = v
        self.__dict__.update(state)

    def append(self):
        additional_text = input("Enter additional text: \n")
        self.text += f"({get_now()}) {additional_text}"
        self.saved = False
