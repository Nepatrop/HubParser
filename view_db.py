import sqlite3

def generate_html():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM articles")
    rows = cursor.fetchall()

    rows.reverse()

    html_content = """
    <html>
    <head>
        <title>Articles</title>
    </head>
    <body>
        <h1>Articles</h1>
        <table border="1">
            <tr>
                <th>Title</th>
                <th>Date</th>
                <th>Link</th>
                <th>Author</th>
                <th>Author Link</th>
                <th>Content</th>
            </tr>
    """

    for row in rows:
        title, date, link, author_name, author_link, content = row
        html_content += f"""
            <tr>
                <td>{title}</td>
                <td>{date}</td>
                <td><a href="{link}">{link}</a></td>
                <td>{author_name}</td>
                <td><a href="{author_link}">{author_link}</a></td>
                <td>{content.replace('<br>', '<br>')}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open('articles.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    cursor.close()
    conn.close()

    print("HTML-страница успешно сгенерирована.")

if __name__ == "__main__":
    generate_html()