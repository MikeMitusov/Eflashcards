from card import Card
from card import data
from rich.console import Console
import random


console = Console()


class CardFeatures(Card):
    def add_group(self, group_name):
        if group_name not in data:
            data[group_name] = {}
        else:
            console.print("[red bold] This group already exists")

    def delete(
        self,
        group=None,
        fcard=None,
        del_fcard=False,
        del_group=False,
        del_all=False,
        warn=False,
    ):
        if del_fcard:
            del data[group][fcard]

        elif del_group:
            del data[group]

        elif del_all and warn:
            user_warn = input("YY: yes; n: no - ")
            if user_warn == "YY":
                for el in list(data):
                    del data[el]
            elif user_warn == "n":
                return print("Canceled")

        elif del_all:
            for el in list(data):
                del data[el]

    def read_word(
        self,
        fcard=None,
        group=None,
        user=False,
    ):
        if user:
            for el in data[group].keys():
                if fcard == el:
                    console.print(el)
                    user_cmd = input(
                        """               
a: answer
m: menu
---------
Command:                                  
"""
                    )
                    if user_cmd == "a":
                        for k, v in data[group].items():
                            if fcard == el:
                                console.print(f"{k} - {v}")

        elif not user:
            text = f"{fcard} - {data[group][fcard]}"
            return text  # here's a problem

    def read_group(self, group=None, user=False, play=True):
        if user:
            while play:
                for fc in data[group]:
                    print(fc)
                    user_cmd = input(
                        """
a: answer
m: menu
---------
Command: """
                    )
                    if user_cmd == "a":
                        console.print(f"[yellow bold] {fc} - {data[group][fc]}")
                        input("Press ENTER to continue... ")

                play = False

        elif not user:
            return data[group]

    def read_all(self):
        for i in data:
            for el in data[i]:
                console.print("[yellow bold]" + el)
                cmd = input("Press ENTER to show answer; m: menu ")
                print("")

                if "m" in cmd:
                    return None

                console.print(f"[yellow bold]{el} - {data[i][el]}" + "\n")
                input("Press ENTER to continue..." + "\n")

    def read_random(self, is_group=False, is_fcard=False):
        if is_group:
            random_key = random.choice(list(data.keys()))

            for i in data[random_key]:
                console.print(f"[yellow bold]{i}")
                cmd = input("Press ENTER to show answer; m: menu ")
                print("")

                if "m" in cmd:
                    return None

                console.print(f"[yellow bold]{i} - {data[random_key][i]}" + "\n")
                input("Press ENTER to continue..." + "\n")

        if is_fcard:
            random_key = random.choice(list(data.keys()))
            random_card = random.choice(list(data[random_key].keys()))

            console.print("[yellow bold]" + random_card)
            cmd = input("Press ENTER to show answer; m: menu ")
            print("")

            if "m" in cmd:
                return None

            console.print(
                f"[yellow bold]{random_card} - {data[random_key][random_card]}" + "\n"
            )
            input("Press ENTER to continue..." + "\n")

    def export_to_md(self, filename):
        with open(filename + ".md", "w") as f:
            for group in data:
                f.write(f"# {group} \n")
                for el in data[group]:
                    f.write(f"{el} - {data[group][el]}" + "\n")

    def translate_text(self, text, from_lang, to_lang):
        from reverso_api.context import ReversoContextAPI

        self.target = ""

        get_translate = ReversoContextAPI(
            source_text=text,
            target_text=self.target,
            source_lang=from_lang,
            target_lang=to_lang,
        )

        translation = list(get_translate.get_translations())

        return translation[0].translation

    def docs(self):
        from rich.markdown import Markdown

        with open("README.md", "r") as f:
            text = f.read()
            md = Markdown(text)

            return md

    def fast_read(self, group):
        for el in data[group]:
            console.print(f"[green] {el} -> {data[group][el]}")

    def read_all_fast(self):
        for i in data:
            for el in data[i]:
                console.print(f"[green]{el} - {data[i][el]}")

    def change_group(self, old_group, new_group):
        data[new_group] = data[old_group]
        del data[old_group]

    def change_card(
        self, group, new_ftext, new_btext=None, old_ftext=None, is_btext_the_same=False
    ):
        if not is_btext_the_same:
            data[group][new_ftext] = new_btext
            del data[group][old_ftext]
        if is_btext_the_same:
            data[group][new_ftext] = data[group][old_ftext]
            del data[group][old_ftext]
