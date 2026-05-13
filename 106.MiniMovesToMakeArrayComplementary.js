
var minMoves = function(nums, limit) {
    
    const n = nums.length;

    const diff = new Array(2 * limit + 2).fill(0);

    for (let i = 0; i < n / 2; i++) {

        let a = Math.min(nums[i], nums[n - 1 - i]);
        let b = Math.max(nums[i], nums[n - 1 - i]);

        diff[a + 1] -= 1;
        diff[b + limit + 1] += 1;

        diff[a + b] -= 1;
        diff[a + b + 1] += 1;
    }

    const pairs = Math.floor(n / 2);

    let current = pairs * 2;

    let answer = Number.MAX_SAFE_INTEGER;

    for (let sum = 2; sum <= 2 * limit; sum++) {

        current += diff[sum];

        answer = Math.min(answer, current);
    }

    return answer;
};