from openai import OpenAI
from config import OPENAI_API_KEY







# Temporary manual version for offline/testing use
def generate_explanation(problem_text: str) -> str:
    return """Step-by-step Explanation:
1. Identify what the problem is asking.
2. Consider brute-force solutions first, then optimize.
3. For array sum problems, using a hash map often improves efficiency.
4. Iterate through the data, check for needed complements.
5. Return the result indices or values.

Python Solution:
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

Time and Space Complexity:
- Time Complexity: O(n), single pass through array.
- Space Complexity: O(n), for hash map storage."""


# # Initialize the new client
# client = OpenAI(api_key=OPENAI_API_KEY)

# def generate_explanation(problem_text: str) -> str:
#     prompt = f"""
#     Read the following LeetCode problem and generate:
#     1. Step-by-step explanation
#     2. Python solution code
#     3. Time and space complexity analysis

#     Problem:
#     {problem_text}
#     """
    
#     response = client.chat.completions.create(
#         model="gpt-5-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful programming tutor."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=700
#     )
    
#     return response.choices[0].message.content.strip()
