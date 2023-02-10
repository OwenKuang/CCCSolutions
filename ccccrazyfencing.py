x = int(input())
heights = input().split()
widths = input().split()
placeholder = 0
totalpaint = 0 
for i in range(x):
    if int(heights[i + 1]) > int(heights[i]):
        placeholder = int(heights[i])
        totalpaint += (placeholder * int(widths[i]))
        triangle = ((int(heights[i + 1]) - placeholder) * int(widths[i]))/2
        totalpaint +=  triangle
    elif int(heights[i]) > int(heights[i+1]):
        placeholder = int(heights[i + 1])
        totalpaint += ( placeholder * int(widths[i]))
        triangle = ((int(heights[i]) - placeholder) * int(widths[i]))/2
        totalpaint += triangle
    else: 
        totalpaint += int(heights[i]) * int(widths[i])

print(totalpaint)
