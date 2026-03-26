class AnnalynsInfiltration {
    public static boolean canFastAttack(boolean knightIsAwake) {
        return !knightIsAwake;
    }

    public static boolean canSpy(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake) {
        return (knightIsAwake || archerIsAwake || prisonerIsAwake);
    }

    public static boolean canSignalPrisoner(boolean archerIsAwake, boolean prisonerIsAwake) {
        return (archerIsAwake == false && prisonerIsAwake == true);
    }

    public static boolean canFreePrisoner(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake, boolean petDogIsPresent) {
        boolean canBeFreed = false;

        if (petDogIsPresent) {
            if (!archerIsAwake) {
                canBeFreed = true;
            } else if (archerIsAwake) {
                canBeFreed = false;
            }
        } else {
            if (prisonerIsAwake) {
                if (archerIsAwake || knightIsAwake) {
                    canBeFreed = false;
                } else {
                    canBeFreed = true;
                }
            }
        }

        return canBeFreed;
    }
}
