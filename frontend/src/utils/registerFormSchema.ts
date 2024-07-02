import { z } from "zod";

export const registerFormSchema = z
    .object({
        email: z.string().email(),
        username: z.string().min(3),
        password: z
            .string()
            .min(8)
            .refine((data) => /\d/.test(data), {
                message: "Password must contain at least one number",
            }),
        confirmPassword: z.string().min(8),
    })
    .refine((data) => data.password === data.confirmPassword, {
        message: "Passwords do not match",
        path: ["confirmPassword"],
    });
