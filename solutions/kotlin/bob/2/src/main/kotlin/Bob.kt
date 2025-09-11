object Bob {
    fun hey(input: String): String {
        val trimmed = input.trimEnd()
        val isQuestion = trimmed.endsWith("?")
        // we´re checking below if the input is formed by letters and if they are in uppercase
        val isYelling = trimmed.any{ it.isLetter()} && trimmed.uppercase() == trimmed
        val isSilence = trimmed.isEmpty()

        // when is equivalent a if, else if, else in Python
        return when {
            isSilence -> "Fine. Be that way!"
            isYelling && isQuestion -> "Calm down, I know what I'm doing!"
            isQuestion -> "Sure."
            isYelling -> "Whoa, chill out!"
            else -> "Whatever."
        }
    }
}