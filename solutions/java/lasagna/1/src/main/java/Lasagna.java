public class Lasagna {
    int expected = 40;
    int preparation = 2;
    
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven() {
        return expected;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int remaining) {
        return (expected - remaining);
    }
    
    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layers) {
        int preparationTime = layers * preparation;
        return preparationTime;
    }
    
    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layers, int oven) {
        int preparationTime = layers * preparation;
        int totalTime = preparationTime + oven;
        return totalTime;
    }
    
}