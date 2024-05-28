# 0x00 Pascal's Triangle

Welcome to the Pascal's Triangle project! This project is part of the ALX Interview preparation series, designed to help you understand and implement algorithms commonly encountered in technical interviews.

## Table of Contents

- [Overview](#overview)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

Pascal's Triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it. This project focuses on generating Pascal's Triangle for a given number of rows.

## File Descriptions

- `0-pascal_triangle.py`: Contains the main function `pascal_triangle(n)` that generates Pascal's Triangle with `n` rows.
- `0-main.py`: Test script to demonstrate the usage of the `pascal_triangle(n)` function.

## Usage

To generate Pascal's Triangle, follow these steps:

1. **Clone the repository**
    ```bash
    git clone https://github.com/mwanikigachanja/alx-interview.git
    ```
2. **Navigate to the project directory**
    ```bash
    cd alx-interview/0x00-pascal_triangle
    ```
3. **Run the test script**
    ```bash
    python3 0-main.py
    ```

## Examples

Here's an example of how the `pascal_triangle(n)` function works:

### Code
```python
from 0-pascal_triangle import pascal_triangle

print(pascal_triangle(5))
```

### Output
```plaintext
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Contributing

Contributions are welcome! If you have any improvements, suggestions, or bug fixes, please follow these steps:

1. **Fork the repository**
2. **Create a new branch**
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit your changes**
    ```bash
    git commit -m "Description of your changes"
    ```
4. **Push to the branch**
    ```bash
    git push origin feature-branch
    ```
5. **Open a pull request** on the main repository

Please ensure your contributions adhere to the existing coding style and include appropriate test coverage.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Explore the project and use it to understand how Pascal's Triangle is generated. Happy coding!

---

[GitHub Repository](https://github.com/mwanikigachanja/alx-interview.git)