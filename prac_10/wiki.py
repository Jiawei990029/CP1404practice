import wikipedia

# def search_wiki(page_title):
#     try:
#         page = wikipedia.page(page_title, auto_suggest=False)
#         print(page)
#     except wikipedia.exceptions.DisambiguationError:
#         pass
#     except wikipedia.exceptions.PageError:
#         pass
#     except Exception:
#         pass
# search_wiki("Python")
# search_wiki("jcu")


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        search_wikipedia(title)
        title = input("Enter page title: ").strip()
    print("Thank you.")

def search_wikipedia(title):
    try:
        wikipedia.set_lang("en")
        page = wikipedia.page(title, auto_suggest=False)
        print(f"\n{page.title}")
        print(page.summary)
        print(f"{page.url}\n")

    except wikipedia.exceptions.DisambiguationError as i:
        print(f"\nWe need a more specific title. Try one of the following, or a new search:")
        print(f"{i.options[:5]}\n")

    except wikipedia.exceptions.PageError:
        print(f"\nPage id \"{title}\" does not match any pages. Try another id!\n")

    except Exception as i:
        print(f"\nAn error occurred: {i}\n")

main()