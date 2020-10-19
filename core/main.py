def colour(color):
	colours = {"NON": "\033[0m",
	"GR": "\033[90m",
	"R": "\033[91m",
	"G": "\033[92m",
	"Y":  "\033[93m",
	"B": "\033[94m"}
	return colours[color]

def banner():
	print (f"""{colour('R')}
██████╗░░█████╗░████████╗░██████╗░███████╗███╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝░██╔════╝████╗░██║
██████╦╝██║░░██║░░░██║░░░██║░░██╗░█████╗░░██╔██╗██║
██╔══██╗██║░░██║░░░██║░░░██║░░╚██╗██╔══╝░░██║╚████║
██████╦╝╚█████╔╝░░░██║░░░╚██████╔╝███████╗██║░╚███║
╚═════╝░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝
{colour('NON')}
""")
