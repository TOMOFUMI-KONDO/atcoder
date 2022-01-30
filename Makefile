all: main.py

define TEMPLATE
def main():
	pass

if __name__ == "__main__":
	main()
endef
export TEMPLATE

main.py:
	echo "$$TEMPLATE" > main.py