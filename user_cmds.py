import card
import features
from rich.console import Console
from rich.panel import Panel
import sys


console = Console()


def status_success():
    console.print("[green] Success!")


def status_error():
    console.print("[red] Error!")


def cg():
    fcard = features.CardFeatures()
    fcard.add_group(input("Group name: "))
    fcard.save()


def cf():
    fcard = features.CardFeatures()
    fcard.add_card(
        input("Group Name: "),
        input("Card text (fluent language): "),
        input("Card text (foreign language): "),
    )
    fcard.save()


def dg():
    fcard = features.CardFeatures()
    fcard.delete(group=input("Name of the Group: "), del_group=True)
    fcard.save()


def df():
    fcard = features.CardFeatures()
    fcard.delete(fcard=input("Name of the Card (fluent language): "), del_fcard=True)
    fcard.save()


def dd():
    fcard = features.CardFeatures()
    fcard.delete(del_all=True, warn=True)
    fcard.save()


def rg():
    fcard = features.CardFeatures()
    fcard.read_group(group=input("Name of the Group: "), user=True)


def rf():
    fcard = features.CardFeatures()
    fcard.read_word(
        group=input("Name of the Group: "),
        fcard=input("Name of the Card (fluent language): "),
        user=True,
    )


def re():
    fcard = features.CardFeatures()
    fcard.read_all()


def rrg():
    fcard = features.CardFeatures()
    fcard.read_random(is_group=True)


def rrf():
    fcard = features.CardFeatures()
    fcard.read_random(is_fcard=True)


def em():
    fcard = features.CardFeatures()
    fcard.export_to_md(input("Filename: "))


def tt():
    fcard = features.CardFeatures()

    text = input("Text: ")
    from_lang = input("From language (example: en): ")
    to_lang = input("Translate to (example: uk): ")

    phrase = fcard.translate_text(
        text=text,
        from_lang=from_lang,
        to_lang=to_lang,
    )

    console.print(f"[yellow bold] {text} --> {phrase}")


def dcs():
    fcard = features.CardFeatures()
    docs = fcard.docs()

    console.print(docs)


def rgf():
    text = input("Group: ")
    fcard = features.CardFeatures()
    fcard.fast_read(text)


def req():
    text = input("Group: ")
    fcard = features.CardFeatures()
    fcard.read_all_fast()


def cgn():
    name = input("Group: ")
    new_name = input("New Group name: ")
    fcard = features.CardFeatures()
    fcard.change_group(name, new_name)

    fcard.save()


def cfn():
    fcard = features.CardFeatures()

    group = input("Group: ")
    old_ftext = input("Old flash card front text: ")
    new_ftext = input("New flash card front text: ")
    the_same_text = input("Do you want the same back text? yes, no: ")
    if the_same_text.strip().lower() == "yes":
        the_same_text = True

        fcard.change_card(
            group=group,
            old_ftext=old_ftext,
            new_ftext=new_ftext,
            is_btext_the_same=the_same_text,
        )

    else:
        the_same_text = False
        new_btext = input("New flash card back text: ")

        fcard.change_card(
            group=group,
            old_ftext=old_ftext,
            new_ftext=new_ftext,
            new_btext=new_btext,
            is_btext_the_same=the_same_text,
        )

    fcard.save()
