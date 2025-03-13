// Accepts any type of value
// If of type number, rounds to provided number of decimal places.
// Otherwise, returns the unmodified value
export const roundToDecimals = (value: any, decimalPlaces: number = 0) => {
    if (typeof value === "number") {
        return Number(value.toFixed(decimalPlaces));
    }
    return value;
}

// Recursively modifies a provided Json and/or Array(s).
// Currently rounds decimals in the provided Json response,
// however the modifying method can be substituded as required.
export const modifyData = (data) => {
    if (Array.isArray(data)) {
        return data.map((value) => modifyData(value));
    } else if (typeof data === "object" && data !== null) {
        const result = {};
        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                result[key] = modifyData(data[key]);
            }
        }
        return result;
    } else {
        // Swap this method to change modification logic.
        return roundToDecimals(data, 8);
    }
};

// Epsilon margin of error for comparing two numbers
const epsilonComparison = (a: number, b: number, epsilon: number = 0): boolean => {
    return Math.abs(a - b) < epsilon;
}