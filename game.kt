fun main() {
    val randomNumber = (1..100).random()
    var attempts = 0
    val maxAttempts = 5

    println("Добро пожаловать в игру! Угадайте число от 1 до 100.")
    
    while (attempts < maxAttempts) {
        println("Введите вашу догадку:")
        val userGuess = readLine()?.toIntOrNull()
        
        if (userGuess == null) {
            println("Пожалуйста, введите корректное число.")
            continue
        }

        attempts++
        
        when {
            userGuess < randomNumber -> println("Слишком мало! Осталось попыток: ${maxAttempts - attempts}")
            userGuess > randomNumber -> println("Слишком много! Осталось попыток: ${maxAttempts - attempts}")
            else -> {
                println("Поздравляем! Вы угадали число $randomNumber за $attempts попыток.")
                return
            }
        }
    }

    println("К сожалению, вы не угадали. Загаданное число было: $randomNumber.")
}
