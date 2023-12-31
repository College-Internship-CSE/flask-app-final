from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show/heads')
def heads():
    head_data = {'IoT , ML, and Security': 'Dr. Mamatha Balachandra',
                 'Data Analytics': 'Dr. U. Dinesh Acharya, Dr. Krishnamoorthi M',
                 'Computer Networks': 'Dr. Aditya Bhakshi',
                 'Web Application Security': 'Dr. G. Deepa',
                 'Security, Computer Vision': 'Dr. Renuka A.',
                 'High Performance Computing, ANN & DL': 'Dr. N. Gopalakrishna Kini',
                 'Natural Language Processing, Model based Analysis': 'Dr. Ashalatha Nayak',
                 'Data Mining': 'Dr. Geetha M., Dr. Harish S V',
                 'Computer Vision & ML': 'Dr. Narendra V.G., Dr. R. Vijaya Arjunan',
                 'Cyber Security and Quantum Computing': 'Dr. Vivekanand Bhat'
                }
        
      

    member_data = {'IoT , ML, and Security': ['Dr.T.Sujithra', 'Dr. Mamatha Balachandra', 'Radhika Kamath', 'Deepthi S'],
                      'Data Analytics': ['Dr. Neelima Bayyapu', 'Mr. Roshan David Jathanna', 'Ms. Musica Supriya', 'Rajashree Krishna'],
                      'Computer Networks': ['Manoj R', 'Dr. Aditya Bakshi'],
                      'Web Application Security': ['Dr. G. Deepa', 'Ms. Anjana S'],
                      'Security, Computer Vision': ['Dr. Hemalatha S.', 'Dr. Radhakrishna Bhat', 'Dr. Renuka A'],
                      'High Performance Computing, ANN & DL': ['Ashwath Rao B', 'N Gopalakrishna Kini', 'Rajesh G'],
                      'Natural Language Processing, Model based Analysis': ['Jimcymol James', 'Ashalatha Nayak'],
                      'Data Mining': ['Anup Bhat B'],
                      'Computer Vision & ML': ['Ms D Cenitta', 'Vidya Prakash'],
                      'Cyber Security and Quantum Computing': ['Dr. Vivekanand Bhat']}
    
    

    return render_template('heads.html', heads=head_data, members= member_data)


@app.route('/show/<string:name>/<int:s_num>')
def display(name, s_num):
    file_dict = {'book': {'directory': '5.8.1.3 Book or Book Chapters.xlsx', 'skiprows': 4},
                 'journal': {'directory': '5.8.1.1 Journal Publications.xlsx', 'skiprows': 5},
                 'conference': {'directory': '5.8.1.2 Conference Proceedings.xlsx', 'skiprows': 5},
                 'patent': {'directory': '5.8.1.4 Patents.xlsx', 'skiprows': 4},
                 'phd': {'directory': '5.8.1.5 PhD Guided.xlsx', 'skiprows': 4}}

    file_cols = {'book': ['Author names as \nappear in paper', 'Title of the chapter', 'Name of the book'],
                 'journal': ['Author names as \nappear in paper', 'Name of the Journal', 'Title of Publication'],
                 'conference': ['Author names as \nappear in paper', 'Conference name', 'Title of paper'],
                 'patent': ['Name of the Faculty', 'Title of the patent\napplication', 'Patent office'],
                 'phd': ['Name of the Student', 'Thesis title', 'Name of the Guide']}

    file_name = file_dict[name]['directory']
    file_path = f'excel_files/{file_name}'

    skiprows = file_dict[name]['skiprows']

    sheet_index = s_num
    df = pd.read_excel(file_path, skiprows=skiprows, sheet_name=sheet_index)
    # Add the column names you wish to display
    selected_columns = file_cols[name]

    df = df[selected_columns]
    df = df.dropna()
    df = df.rename(columns={
                   selected_columns[0]: 'A', selected_columns[1]: 'B', selected_columns[2]: 'C'})

    # print(df)

    data = df.to_dict(orient='records')

    return render_template('display.html', data=data, selected_columns=selected_columns, name=name)


if __name__ == '__main__':
    app.run(debug=True, port=3000)



  # 'Biometrics, Software Engineering': 'Dr. Srikanth Prabhu',
        #          'Computer Aided Diagnosis & Assistive Technologies': 'Dr. P.C. Siddalingaswamy ',
        #          'Computer Vision & ML': 'Dr. Narendra V.G., Dr. R. Vijaya Arjunan',
        #          'Data Analytics': 'Dr. Dr. U. Dinesh Acharya, Dr. Krishnamoorthi M',
        #          'Data Mining': 'Dr. Geetha M., Dr. Harish S V',
        #          'High Performance Computing Systems, ANN & DL': 'Dr. N. Gopalakrishna Kini',
        #          'Natural Language Processing, Model based Analysis': 'Dr. Ashalatha Nayak',
        #          'Security, ML and DL': 'Dr. Prema K V',
        #          'Security, Computer Vision': 'Dr. Renuka A.'