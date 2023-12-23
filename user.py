from rich.console import Console
from rich.panel import Panel
import sys
import user_cmds

console = Console(width=50)

logo_text = "[white bold] EasyCards [/white bold]"

text_navigation = """
[blue bold]-----Create and change & Delete-----[/blue bold]
cg: create group
cf: create flash card
dg: delete group
df: delete flash card
dd: delete everything
cgn: change group
cfn: change flash card

[green bold]-----Read-----[/green bold]
rg: read group
rf: read flash card
re: read everything
rrg: read random group
rrf: read random flash card
rgf: read group quickly
req: read everything quickly

[white bold]-----Translation and other-----[/white bold]
tt: translate text

[red bold]-----Exit & Export-----[/red bold]
m: menu (navigation)
dcs: app documentation
em: export to markdown (md)
ee: exit


[yellow]Created by MikeMits. EasyCard v0.4.0-beta[/yellow]
"""

console.print(logo_text, justify="center", style="yellow on blue")
console.print(Panel(text_navigation))

turned = True
while turned:
    try:
        cmd = input("Command: ").strip().lower()
        if cmd == "cg":
            user_cmds.cg()

        elif cmd == "cf":
            user_cmds.cf()

        elif cmd == "dg":
            user_cmds.dg()

        elif cmd == "df":
            user_cmds.df()

        elif cmd == "dd":
            user_cmds.dd()

        elif cmd == "rg":
            user_cmds.rg()

        elif cmd == "rf":
            user_cmds.rf()

        elif cmd == "re":
            user_cmds.re()

        elif cmd == "rrg":
            user_cmds.rrg()

        elif cmd == "rrf":
            user_cmds.rrf()

        elif cmd == "em":
            user_cmds.em()

        elif cmd == "tt":
            user_cmds.tt()

        elif cmd == "dcs":
            user_cmds.dcs()

        elif cmd == "rgf":
            user_cmds.rgf()

        elif cmd == "req":
            user_cmds.req()

        elif cmd == "cgn":
            user_cmds.cgn()

        elif cmd == "cfn":
            user_cmds.cfn()

        elif cmd == "m":
            console.print(logo_text, justify="center", style="yellow on blue")
            console.print(Panel(text_navigation))

        elif cmd == "ee":
            sys.exit()
        else:
            console.print("[red]Incorrect command!")
    except Exception:
        console.print("[red]Error!")
