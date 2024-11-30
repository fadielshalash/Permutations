class Solution:
    def permute(self, strings: list[str]) -> list[list[str]]:
        result = []

        if len(strings) == 1:
            return [strings.copy()]

        for i in range(len(strings)):
            n = strings.pop(0)  
            my_perms = self.permute(strings)  

            for perms in my_perms:
                perms.append(n)  
            result.extend(my_perms) 

            strings.append(n)

        return result


def main():
    chars = ['a', 'b', 'c']
    solution = Solution()
    permutations = solution.permute(chars)
    print("Permutations of", chars, "are:")
    for perm in permutations:
        print(perm)


if __name__ == "__main__":
    main()
