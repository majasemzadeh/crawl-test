from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        def log_request(route, request):

            if request.url.startswith("https://maktabkhooneh.org/api/"):
                print(request.url)
            route.continue_()

        context.route('**/*', log_request)

        page = context.new_page()
        page.goto('https://maktabkhooneh.org/learn/management-business/')
        page.wait_for_timeout(5000)

        browser.close()


if __name__ == '__main__':
    main()
