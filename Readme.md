# Save the README content to a file for download
readme_content = """
## README.md

### Maktabkhooneh Course Categories Data Fetcher

This script is designed to fetch course data from the Maktabkhooneh platform.
can you write it in a string in a python code ?I!
#### How it Works:
Install the required Python packages:


1. **Setting Up**:
   - Two main libraries, `requests` and `json`, are imported.
   - An empty list called `all_responses` is initialized to store data fetched from the API.

2. **Functionality**:
   - The `extract_data(slug)` function is defined to fetch data for a given category (identified by its slug) and its child categories. It does this recursively to ensure all levels of subcategories are fetched.
   - For each category slug provided, the function sends a `GET` request to the Maktabkhooneh API endpoint to fetch the course's data. The response is then appended to the `all_responses` list.
   - If the category has child categories, the function calls itself for each child, ensuring that data for all subcategories is also fetched.

3. **Execution**:
   - The script fetches a list of root categories from the Maktabkhooneh API.
   - For each root category, the `extract_data(slug)` function is called to fetch its data and the data of its subcategories.
   - Finally, all fetched data is saved to a file named `all_data.json` with appropriate formatting.

#### Usage:

To use the script, simply run it. Ensure you have the `requests` library installed. The output will be saved in a file named `all_data.json`.
"""

