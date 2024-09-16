class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        # Initialize two dictionaries
        t_count = Counter(t)  # Count of characters in t
        window_count = Counter()  # Count of characters in current window

        # Initialize variables
        left = 0
        min_window = ""
        min_length = float('inf')
        required = len(t_count)
        formed = 0

        # Iterate through s with right pointer
        for right in range(len(s)):
            # Add the current character to window_count
            char = s[right]
            window_count[char] += 1

            # Check if this character completes a required character count
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Try to contract the window from the left
            while formed == required and left <= right:
                # Update the minimum window if necessary
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]

                # Remove the leftmost character from the window
                char = s[left]
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                left += 1

        return min_window