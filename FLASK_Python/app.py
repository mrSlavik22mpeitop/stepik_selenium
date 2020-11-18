from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie
from database_setup import Base, Branch
from database_setup import Base, Screening
from database_setup import Base, Seat
from database_setup import Base, User

app = Flask(__name__)

engine = create_engine('sqlite:///books-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Movie CLASS
#Movie CLASS
#Movie CLASS
#Movie CLASS
#Movie CLASS
@app.route('/')
def showGeneral():
    return render_template("general.html")

@app.route('/movies')
def showMovies():
    movies = session.query(Movie).all()
    return render_template("movies.html", movies=movies)


@app.route('/movies/new/', methods=['GET', 'POST'])
def newMovie():
    if request.method == 'POST':
        newMovie = Movie(title=request.form['name'], author=request.form['author'], genre=request.form['genre'], price=request.form['price'])
        session.add(newMovie)
        session.commit()
        return redirect(url_for('showMovies'))
    else:
        return render_template('newMovie.html')

    # Эта функция позволит нам обновить книги и сохранить их в базе данных.
@app.route("/movies/<int:movie_id>/edit/", methods=['GET', 'POST'])
def editMovie(movie_id):
    editedMovie = session.query(Movie).filter_by(id=movie_id).one()
    if request.method == 'POST':
        if request.form['name'] or request.form['author'] or request.form['genre'] or request.form['price']:
            editedMovie.title = request.form['name']
            editedMovie.author = request.form['author']
            editedMovie.genre = request.form['genre']
            editedMovie.price = request.form['price']
            return redirect(url_for('showMovies'))
    else:
        return render_template('editMovie.html', movie=editedMovie)

    # Эта функция для удаления книг
@app.route('/movies/<int:movie_id>/delete/', methods=['GET', 'POST'])
def deleteMovie(movie_id):
    movieToDelete = session.query(Movie).filter_by(id=movie_id).one()
    if request.method == 'POST':
        session.delete(movieToDelete)
        session.commit()
        return redirect(url_for('showMovies', movie_id=movie_id))
    else:
        return render_template('deleteMovie.html', movie=movieToDelete)
#Movie CLASS
#Movie CLASS
#Movie CLASS
#Movie CLASS
#Movie CLASS




#Branch CLASS
#Branch CLASS
#Branch CLASS
#Branch CLASS
#Branch CLASS
@app.route('/branchs')
def showBranchs():
    branchs = session.query(Branch).all()
    return render_template("branch.html", branchs=branchs)


@app.route('/branchs/new/', methods=['GET', 'POST'])
def newBranch():
    if request.method == 'POST':
        newBranch = Branch(name=request.form['name'], seats=request.form['seats'])
        session.add(newBranch)
        session.commit()
        return redirect(url_for('showBranchs'))
    else:
        return render_template('newBranch.html')


@app.route("/branchs/<int:branch_id>/edit/", methods=['GET', 'POST'])
def editBranch(branch_id):
    editedBranch = session.query(Branch).filter_by(id=branch_id).one()
    if request.method == 'POST':
        if request.form['name'] or request.form['seats']:
            editedBranch.name = request.form['name']
            editedBranch.seats = request.form['seats']
            return redirect(url_for('showBranchs'))
    else:
        return render_template('editBranch.html', branch=editedBranch)

@app.route('/branchs/<int:branch_id>/delete/', methods=['GET', 'POST'])
def deleteBranch(branch_id):
    branchToDelete = session.query(Branch).filter_by(id=branch_id).one()
    if request.method == 'POST':
        session.delete(branchToDelete)
        session.commit()
        return redirect(url_for('showBranchs', branch_id=branch_id))
    else:
        return render_template('deleteBranch.html', branch=branchToDelete)
#Branch CLASS
#Branch CLASS
#Branch CLASS
#Branch CLASS
#Branch CLASS



#Screenings CLASS
#Screenings CLASS
#Screenings CLASS
#Screenings CLASS
#Screenings CLASS
@app.route('/screenings')
def showScreenings():
    screenings = session.query(Screening).all()
    return render_template("screenings.html", screenings=screenings)


@app.route('/screenings/new/', methods=['GET', 'POST'])
def newScreening():
    if request.method == 'POST':
        newScreening = Screening(movie_id=request.form['movie_id'], branch_id=request.form['branch_id'], screening_time=request.form['screening_time'])
        session.add(newScreening)
        session.commit()
        return redirect(url_for('showScreenings'))
    else:
        movies = session.query(Movie).all()
        branchs = session.query(Branch).all()
        return render_template('newScreening.html', branchs=branchs, movies=movies)



@app.route("/screenings/<int:screening_id>/edit/", methods=['GET', 'POST'])
def editScreening(screening_id):
    editedScreening = session.query(Screening).filter_by(id=screening_id).one()
    if request.method == 'POST':
        if request.form['movie_id'] or request.form['branch_id'] or request.form['screening_time']:
            editedScreening.movie_id = request.form['movie_id']
            editedScreening.branch_id = request.form['branch_id']
            editedScreening.screening_time = request.form['screening_time']
            return redirect(url_for('showScreenings'))
    else:
        return render_template('editScreening.html', screening=editedScreening)

@app.route('/screenings/<int:screening_id>/delete/', methods=['GET', 'POST'])
def deleteScreening(screening_id):
    screeningToDelete = session.query(Screening).filter_by(id=screening_id).one()
    if request.method == 'POST':
        session.delete(screeningToDelete)
        session.commit()
        return redirect(url_for('showScreenings', screening_id=screening_id))
    else:
        return render_template('deleteScreening.html', screening=screeningToDelete)
#Screenings CLASS
#Screenings CLASS
#Screenings CLASS
#Screenings CLASS
#Screenings CLASS


#CLASS Seat
#CLASS Seat
#CLASS Seat
#CLASS Seat
#CLASS Seat
@app.route('/seats')
def showSeats():
    seats = session.query(Seat).all()
    return render_template("seats.html", seats=seats)


@app.route('/seats/new/', methods=['GET', 'POST'])
def newSeat():
    if request.method == 'POST':
        newSeat = Seat(row=request.form['row'], number=request.form['number'], branch_id=request.form['branch_id'])
        session.add(newSeat)
        session.commit()
        return redirect(url_for('showSeats'))
    else:
        branchs = session.query(Branch).all()
        return render_template('newSeat.html', branchs=branchs)

@app.route("/seats/<int:seat_id>/edit/", methods=['GET', 'POST'])
def editSeat(seat_id):
    editedSeat = session.query(Seat).filter_by(id=seat_id).one()
    if request.method == 'POST':
        if request.form['row'] or request.form['number'] or request.form['branch_id']:
            editedSeat.row = request.form['row']
            editedSeat.number = request.form['number']
            editedSeat.branch_id = request.form['branch_id']
            return redirect(url_for('showSeats'))
    else:
        return render_template('editSeat.html', seat=editedSeat)


@app.route('/seats/<int:seat_id>/delete/', methods=['GET', 'POST'])
def deleteSeat(seat_id):
    seatToDelete = session.query(Seat).filter_by(id=seat_id).one()
    if request.method == 'POST':
        session.delete(seatToDelete)
        session.commit()
        return redirect(url_for('showSeats', seat_id=seat_id))
    else:
        return render_template('deleteSeat.html', seat=seatToDelete)
#CLASS Seat
#CLASS Seat
#CLASS Seat
#CLASS Seat
#CLASS Seat


@app.route('/users')
def showUsers():
    users = session.query(User).all()
    return render_template("users.html", users=users)


@app.route('/users/new/', methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        newUser = User(username=request.form['username'], password=request.form['password'])
        session.add(newUser)
        session.commit()
        return redirect(url_for('showUsers'))
    else:
        return render_template('newUsers.html')


@app.route("/users/<int:user_id>/edit/", methods=['GET', 'POST'])
def editUser(user_id):
    editedUser = session.query(User).filter_by(id=user_id).one()
    if request.method == 'POST':
        if request.form['username'] or request.form['password']:
            editedUser.username = request.form['username']
            editedUser.password = request.form['password']
            return redirect(url_for('showUsers'))
    else:
        return render_template('editUser.html', user=editedUser)


@app.route('/users/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteUser(user_id):
    userToDelete = session.query(User).filter_by(id=user_id).one()
    if request.method == 'POST':
        session.delete(userToDelete)
        session.commit()
        return redirect(url_for('showUsers', user_id=user_id))
    else:
        return render_template('deleteUser.html', user=userToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(port=4996)