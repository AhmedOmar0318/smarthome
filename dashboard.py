from tkinter import *
from api import haal_weer_op

resultaat = haal_weer_op()


def open_main_page():

    main = Tk()
    main.title("Smart Home Dashboard")

    navbar = Frame(main, bg="#333", height=50)
    navbar.pack(fill=X)

    def logout():
        main.destroy()
        login_window.deiconify()

    container = Frame(main)
    container.pack(fill='both', expand=True)

    menu_frame = Frame(container)
    temp_frame = Frame(container)
    cv_frame = Frame(container)
    vent_frame = Frame(container)
    bew_frame = Frame(container)
    weer_frame = Frame(container)

    instellingen_frame = Frame(container)
    apparaten_frame = Frame(container)
    veiligheid_frame = Frame(container)

    for frame in (
        menu_frame, temp_frame, cv_frame, vent_frame, bew_frame, weer_frame,
        instellingen_frame, apparaten_frame, veiligheid_frame
    ):
        frame.place(relwidth=1, relheight=1)


    def show_frame(frame):
        frame.tkraise()

    Button(navbar, text="Logout", bg="#444", fg="white",
           command=logout, width=12).pack(side=LEFT, padx=5, pady=10)

    Button(navbar, text="Instellingen", bg="#444", fg="white",
           command=lambda: show_frame(instellingen_frame), width=12).pack(side=LEFT, padx=5)

    Button(navbar, text="Apparaten", bg="#444", fg="white",
           command=lambda: show_frame(apparaten_frame), width=12).pack(side=LEFT, padx=5)

    Button(navbar, text="Veiligheid", bg="#444", fg="white",
           command=lambda: show_frame(veiligheid_frame), width=12).pack(side=LEFT, padx=5)


    Label(menu_frame, text="Smart Home Menu", font=("Arial", 22)).pack(pady=30)

    Button(menu_frame, text="Temperatuur", font=("Arial", 14),
           command=lambda: show_frame(temp_frame), width=20).pack(pady=10)

    Button(menu_frame, text="CV-ketel", font=("Arial", 14),
           command=lambda: show_frame(cv_frame), width=20).pack(pady=10)

    Button(menu_frame, text="Ventilatie", font=("Arial", 14),
           command=lambda: show_frame(vent_frame), width=20).pack(pady=10)

    Button(menu_frame, text="Bewatering", font=("Arial", 14),
           command=lambda: show_frame(bew_frame), width=20).pack(pady=10)


    Label(temp_frame, text="Temperatuur Beheer", font=("Arial", 20)).pack(pady=20)

    current_temp_label = Label(temp_frame, text=f"Momenteel is het {resultaat}°C", font=("Arial", 18))
    current_temp_label.pack(pady=5)

    current_temp = IntVar(value=20)

    Label(temp_frame, text="Pas temperatuur aan", font=("Arial", 16)).pack()

    def increase_temp():
        current_temp.set(current_temp.get() + 1)
        temp_label.config(text=f"{current_temp.get()}°C")

    def decrease_temp():
        current_temp.set(current_temp.get() - 1)
        temp_label.config(text=f"{current_temp.get()}°C")

    frame_temp_buttons = Frame(temp_frame)
    frame_temp_buttons.pack(pady=5)

    Button(frame_temp_buttons, text="-", width=5, command=decrease_temp).pack(side=LEFT, padx=10)
    Button(frame_temp_buttons, text="+", width=5, command=increase_temp).pack()

    temp_label = Label(temp_frame, text="20°C", font=("Arial", 16))
    temp_label.pack(pady=10)

    Button(temp_frame, text="← Terug naar menu", command=lambda: show_frame(menu_frame)).pack(pady=20)


    Label(cv_frame, text="CV-ketel Instellingen", font=("Arial", 20)).pack(pady=20)

    def set_cv(v):
        cv_label.config(text=f"CV-ketel: {v}%")

    Button(cv_frame, text="0%", width=10, command=lambda: set_cv(0)).pack(pady=5)
    Button(cv_frame, text="50%", width=10, command=lambda: set_cv(50)).pack(pady=5)
    Button(cv_frame, text="100%", width=10, command=lambda: set_cv(100)).pack(pady=5)

    cv_label = Label(cv_frame, text="CV-ketel: 0%", font=("Arial", 16))
    cv_label.pack(pady=20)

    Button(cv_frame, text="← Terug naar menu", command=lambda: show_frame(menu_frame)).pack(pady=20)


    Label(vent_frame, text="Ventilatie Stand", font=("Arial", 20)).pack(pady=20)

    def set_vent(s):
        vent_label.config(text=f"Ventilatie: stand {s}")

    for i in range(1, 5):
        Button(vent_frame, text=f"Stand {i}", width=15, command=lambda x=i: set_vent(x)).pack(pady=5)

    vent_label = Label(vent_frame, text="Ventilatie: stand 1", font=("Arial", 16))
    vent_label.pack(pady=20)

    Button(vent_frame, text="← Terug naar menu", command=lambda: show_frame(menu_frame)).pack(pady=20)


    Label(bew_frame, text="Bewatering Control", font=("Arial", 20)).pack(pady=20)

    def set_bew(s):
        bew_label.config(text=f"Bewatering: {s}")

    Button(bew_frame, text="AAN", width=15, command=lambda: set_bew("AAN")).pack(pady=5)
    Button(bew_frame, text="UIT", width=15, command=lambda: set_bew("UIT")).pack(pady=5)

    bew_label = Label(bew_frame, text="Bewatering: UIT", font=("Arial", 16))
    bew_label.pack(pady=20)

    Button(bew_frame, text="← Terug naar menu", command=lambda: show_frame(menu_frame)).pack(pady=20)



    Label(instellingen_frame, text="Instellingen", font=("Arial", 22)).pack(pady=20)
    Label(instellingen_frame, text="Systeeminstellingen komen hier.", font=("Arial", 16)).pack(pady=10)
    Button(instellingen_frame, text="← Terug naar menu",
           command=lambda: show_frame(menu_frame)).pack(pady=20)


    Label(apparaten_frame, text="Apparaten", font=("Arial", 22)).pack(pady=20)
    Label(apparaten_frame, text="Overzicht van apparaten", font=("Arial", 16)).pack(pady=10)
    Button(apparaten_frame, text="← Terug naar menu",
           command=lambda: show_frame(menu_frame)).pack(pady=20)


    Label(veiligheid_frame, text="Veiligheid", font=("Arial", 22)).pack(pady=20)
    Label(veiligheid_frame, text="Beveiligingsopties komen hier.", font=("Arial", 16)).pack(pady=10)
    Button(veiligheid_frame, text="← Terug naar menu",
           command=lambda: show_frame(menu_frame)).pack(pady=20)


    show_frame(menu_frame)

    main.mainloop()



def login():
    email = email_entry.get()
    password = pass_entry.get()

    if email == "123" and password == "123":
        login_window.withdraw()
        open_main_page()
    else:
        error_label.config(text="Wrong email or password", fg="red")


login_window = Tk()
login_window.title("Login")

Label(login_window, text="Email:").pack(pady=5)
email_entry = Entry(login_window)
email_entry.pack()

Label(login_window, text="Password:").pack(pady=5)
pass_entry = Entry(login_window, show="*")
pass_entry.pack()

Button(login_window, text="Login", command=login).pack(pady=15)

error_label = Label(login_window, text="")
error_label.pack()

login_window.mainloop()


