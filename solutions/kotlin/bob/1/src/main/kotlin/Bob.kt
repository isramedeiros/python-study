object Bob {
    fun hey(input: String): String {
        /*

        variable trimmedEnd trims the input
        variable isYelling is true if both conditions (input trimmed has only letters and its in uppercase )
        
        */
        val trimmedEnd = input.trimEnd()
        val isYelling = trimmedEnd.any { it.isLetter()} && trimmedEnd.uppercase() == trimmedEnd
        
        return when {
           /*
            isBlank() -> checks if the input is empty
            
            isYelling && trimmedEnd.endsWith("?") -> checks if both conditions are true: if the input is yelling and it has a question mark after the trim.

            trimmedEnd.endsWith("?") -> checks only if the trimmed input ends with a question mark (the yelling + question **condition** was already handled)     

            isYelling -> checks only if the input is yelling (has only capital letters). the yelling + question **condition** was already handled
            
            */
            
           input.isBlank() -> "Fine. Be that way!"
           isYelling && trimmedEnd.endsWith("?") -> "Calm down, I know what I'm doing!"
           trimmedEnd.endsWith("?") -> "Sure."
           isYelling -> "Whoa, chill out!"
           else -> "Whatever."
        }
    }
}
