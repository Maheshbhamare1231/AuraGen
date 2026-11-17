
## Design System Version
Version: 0.1 (Provisional)

Note:
This initial design system is based on the
Day 2 generated FinancialForm.jsx.
It will be updated after integration with
the frontend design from Member 2.


# AuraGen UI Design System

## 1. Project Overview

AuraGen generates simplified React user interfaces based on cognitive friction.

All generated components should follow a consistent design system.

## 2. Technology

- React
- JavaScript
- JSX
- Tailwind CSS

## 3. Color Guidelines

Use the following colors for the initial financial form design:

- Primary: blue-600
- Primary Hover: blue-700
- Background: white
- Main Text: gray-800
- Secondary Text: gray-700
- Borders: gray-200 and gray-300

## 4. Typography

- Main headings: text-2xl font-bold
- Labels: text-sm font-medium
- Normal text: text-sm or text-base
- Use gray-800 for important headings.
- Use gray-700 for labels.

## 5. Input Field Guidelines

Every input field should:

- Use full available width.
- Have appropriate labels.
- Have clear borders.
- Have comfortable padding.
- Use rounded corners.
- Include visible focus styling.

Recommended Tailwind classes:

```jsx
className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
```

## 6. Button Guidelines

Buttons should:

- Have clear action text.
- Use a blue primary background.
- Have white text.
- Include hover styling.
- Have rounded corners.
- Be easy to click.

Recommended Tailwind classes:

```jsx
className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700"
```

## 7. Form Layout Guidelines

Use:

- max-w-md for a medium-sized form.
- mx-auto for horizontal centering.
- p-6 for internal spacing.
- space-y-4 between form fields.
- rounded-lg for the form container.
- shadow-md for subtle elevation.
- border border-gray-200 for the container.

## 8. React Component Rules

Generated components must:

- Use valid React JSX.
- Use functional components.
- Use useState when form state is required.
- Use controlled inputs.
- Use meaningful variable and function names.
- Include appropriate labels.
- Include form submission handling when needed.
- Export the main component as default.

## 9. Code Quality Rules

- Generate readable and properly formatted JSX.
- Avoid unnecessary dependencies.
- Avoid inline CSS when Tailwind CSS is sufficient.
- Do not generate incomplete components.
- Do not include explanations outside the requested code output.
- Preserve user-entered form values when simplifying a form.

## 10. Accessibility Guidelines

- Every input must have an associated label.
- Use appropriate input types.
- Use semantic HTML elements.
- Buttons must have clear text.
- Maintain visible keyboard focus indicators.

## 11. AuraGen Generation Objective

When generating a simplified UI:

1. Understand the original form.
2. Identify unnecessary complexity.
3. Reduce the number of visible fields when appropriate.
4. Organize fields into manageable steps if required.
5. Maintain the same design system.
6. Generate valid React JSX.

