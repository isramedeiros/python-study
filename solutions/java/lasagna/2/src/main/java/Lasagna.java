public class Lasagna {
    int expected = 40;
    int preparation = 2;
    
    public int expectedMinutesInOven() {
        return expected;
    }

    public int remainingMinutesInOven(int remaining) {
        return (expected - remaining);
    }
    
    public int preparationTimeInMinutes(int layers) {
        int preparationTime = layers * preparation;
        return preparationTime;
    }
    
    public int totalTimeInMinutes(int layers, int oven) {
        int preparationTime = layers * preparation;
        int totalTime = preparationTime + oven;
        return totalTime;
    }
    
}