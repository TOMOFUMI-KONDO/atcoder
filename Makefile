define TEMPLATE
def main():
	pass

if __name__ == "__main__":
	main()
endef
export TEMPLATE

PATH=""
.PHONY: gen
gen:
	echo "$$TEMPLATE" > $(PATH)