/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    let a= [...args]
    return a.length;
 
};

/**
 * argumentsLength(1, 2, 3); // 3
 */