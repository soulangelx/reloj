Segundos = 0
Minutos = 59
Hora = 12

def on_every_interval():
    global Segundos
    Segundos += 1
loops.every_interval(1000, on_every_interval)

def on_forever():
    global Minutos, Segundos, Hora
    if Segundos > 59:
        Minutos += 1
        Segundos = 0
    elif Minutos > 59:
        Hora += 1
        Minutos = 0
    elif Hora > 12:
        Hora = 1
    else:
        basic.show_string("" + str(Hora) + ":" + str(Minutos) + ":" + str(Segundos))
basic.forever(on_forever)
