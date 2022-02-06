all: main.py

define TEMPLATE
def main():
    N = int(input())


if __name__ == "__main__":
    main()
endef
export TEMPLATE

main.py:
	echo "$$TEMPLATE" > main.py

clean:
	rm -f main.py