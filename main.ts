let Segundos = 0
let Minutos = 59
let Hora = 12
loops.everyInterval(1000, function () {
    Segundos += 1
})
basic.forever(function () {
    if (Segundos > 59) {
        Minutos += 1
        Segundos = 0
    } else if (Minutos > 59) {
        Hora += 1
        Minutos = 0
    } else if (Hora > 12) {
        Hora = 1
    } else {
        basic.showString("" + Hora + ":" + ("" + Minutos) + ":" + ("" + Segundos))
    }
})
