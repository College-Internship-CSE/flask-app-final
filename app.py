from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show/<string:name>/<int:s_num>')
def display(name,s_num):
    file_dict = {'book': {'directory': '5.8.1.3 Book or Book Chapters.xlsx', 'skiprows': 4},
                'journal': {'directory': '5.8.1.1 Journal Publications.xlsx', 'skiprows': 5},
                'conference': {'directory': '5.8.1.2 Conference Proceedings.xlsx', 'skiprows': 5},
                'patent': {'directory': '5.8.1.4 Patents.xlsx', 'skiprows': 4},
                'phd': {'directory': '5.8.1.5 PhD Guided.xlsx', 'skiprows': 4}}
    
    file_cols = {'book': ['Author names as \nappear in paper','Title of the chapter', 'Name of the book'],
                 'journal': ['Author names as \nappear in paper', 'Name of the Journal', 'Title of Publication'],
                 'conference': ['Author names as \nappear in paper', 'Conference name', 'Title of paper'],
                 'patent': ['Name of the Faculty', 'Title of the patent\napplication', 'Patent office'],
                 'phd': ['Name of the \nResearch Scholar', 'Thesis title', 'Name of the Guide']}



    file_name = file_dict[name]['directory']
    file_path = f'excel_files/{file_name}'

    skiprows = file_dict[name]['skiprows']


    sheet_index = s_num
    df = pd.read_excel(file_path, skiprows=skiprows, sheet_name=sheet_index)
    # Add the column names you wish to display
    selected_columns = file_cols[name]

    df = df[selected_columns]
    df = df.dropna()
    df = df.rename(columns={selected_columns[0]: 'A', selected_columns[1]: 'B', selected_columns[2]: 'C'})

    # print(df)

    data = df.to_dict(orient='records')

    return render_template('display.html', data=data, selected_columns= selected_columns, name=name)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
