#!/usr/bin/python3
import argparse

#Create the command-line capability
parser = argparse.ArgumentParser(prog="Snort Rule Maker Script Script", 
				 description=textwrap.dedent('''\
				 This program will take in indicators of compromise and turn them into
				 snort rules automatically.  Currently this script can take in IP addresses,
				 URLs, '''),
				 formatter_class=argparse.RawTextHelpFormatter)
mandatory = parser.add_argument_group("Mandatory",description="These are mandatory.")
optional = parser.add_argument_group("Optional", description="These are optional switches.")
mandatory.add_argument("-i", "--input", help="The path IOC file.", metavar="")
optional = parser.add_argument("-I","--interactive", help="Bring up the interactive prompt.", metavar="")
optional = parser.add_argument("-a","--action",help=textwrap.dedent('''\
				 Use this to specify the action you would like the parser to make.  The default action that the rule
				 maker will use is alert.  With this switch it will change it from alert to reject or drop.  The rule
				 maker will decide which to use depending on your snort settings.''')
args = parser.parse_args()

if __name__ == "__main__":
	main()
else:
	print("This program is ment to be run by itself, not as a module.")

