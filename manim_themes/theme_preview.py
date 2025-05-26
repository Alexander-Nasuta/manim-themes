import manim as m

def theme_preview() -> m.VGroup:
    """
    Create a preview of the theme colors. It is similar to the manim color preview, just ommits the prue colors.
    :return: A VGroup of all the colors in the theme.
    """
    blue_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.BLUE_A)
    blue_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.BLUE_B)
    blue_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.BLUE_C)
    blue_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.BLUE_D)
    blue_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.BLUE_E)
    blue_lines = m.VGroup(blue_a_line, blue_b_line, blue_c_line, blue_d_line, blue_e_line).arrange(m.DOWN, buff=0.4)

    teal_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.TEAL_A)
    teal_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.TEAL_B)
    teal_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.TEAL_C)
    teal_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.TEAL_D)
    teal_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.TEAL_E)
    teal_lines = m.VGroup(teal_a_line, teal_b_line, teal_c_line, teal_d_line, teal_e_line).arrange(m.DOWN, buff=0.4)

    green_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GREEN_A)
    green_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GREEN_B)
    green_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GREEN_C)
    green_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GREEN_D)
    green_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GREEN_E)
    green_lines = m.VGroup(green_a_line, green_b_line, green_c_line, green_d_line, green_e_line).arrange(m.DOWN, buff=0.4)

    yellow_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.YELLOW_A)
    yellow_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.YELLOW_B)
    yellow_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.YELLOW_C)
    yellow_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.YELLOW_D)
    yellow_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.YELLOW_E)
    yellow_lines = m.VGroup(yellow_a_line, yellow_b_line, yellow_c_line, yellow_d_line, yellow_e_line).arrange(m.DOWN, buff=0.4)

    gold_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GOLD_A)
    gold_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GOLD_B)
    gold_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GOLD_C)
    gold_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GOLD_D)
    gold_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.GOLD_E)
    gold_lines = m.VGroup(gold_a_line, gold_b_line, gold_c_line, gold_d_line, gold_e_line).arrange(m.DOWN, buff=0.4)

    red_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.RED_A)
    red_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.RED_B)
    red_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.RED_C)
    red_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.RED_D)
    red_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.RED_E)
    red_lines = m.VGroup(red_a_line, red_b_line, red_c_line, red_d_line, red_e_line).arrange(m.DOWN, buff=0.4)

    maroon_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.MAROON_A)
    maroon_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.MAROON_B)
    maroon_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.MAROON_C)
    maroon_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.MAROON_D)
    maroon_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.MAROON_E)
    maroon_lines = m.VGroup(maroon_a_line, maroon_b_line, maroon_c_line, maroon_d_line, maroon_e_line).arrange(m.DOWN, buff=0.4)

    purple_a_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.PURPLE_A)
    purple_b_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.PURPLE_B)
    purple_c_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.PURPLE_C)
    purple_d_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.PURPLE_D)
    purple_e_line = m.Line(m.ORIGIN, m.RIGHT * 1.5, stroke_width=35, color=m.PURPLE_E)
    purple_lines = m.VGroup(purple_a_line, purple_b_line, purple_c_line, purple_d_line, purple_e_line).arrange(m.DOWN, buff=0.4)


    color_lines = m.VGroup(
        blue_lines,
        teal_lines,
        green_lines,
        yellow_lines,
        gold_lines,
        red_lines,
        maroon_lines,
        purple_lines,
    ).arrange(m.RIGHT, buff=0.1)

    left_col_line_width= m.RIGHT * (1.5 * 4 + 0.1 * 3)
    pink_line = m.Line(m.ORIGIN, left_col_line_width, stroke_width=35, color=m.PINK)
    light_pink_line = m.Line(m.ORIGIN, left_col_line_width, stroke_width=35, color=m.LIGHT_PINK)
    orange_line = m.Line(m.ORIGIN, left_col_line_width, stroke_width=35, color=m.ORANGE)
    light_brown_line = m.Line(m.ORIGIN, left_col_line_width, stroke_width=35, color=m.LIGHT_BROWN)
    dark_brown_line = m.Line(m.ORIGIN, left_col_line_width, stroke_width=35, color=m.DARK_BROWN)
    gray_brown_line = m.Line(m.ORIGIN, left_col_line_width , stroke_width=35, color=m.GRAY_BROWN)

    left_col = m.VGroup(
        pink_line,
        light_pink_line,
        orange_line,
        light_brown_line,
        dark_brown_line,
        gray_brown_line,
    ).arrange(m.DOWN, buff=0.4)

    left_col.next_to(blue_lines, m.DOWN, buff=0.8, aligned_edge=m.LEFT)

    middle_col_line_width = m.RIGHT * (1.5 * 4 + 0.1 * 3)
    white_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.WHITE)
    gray_a_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.GRAY_A)
    gray_b_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.GRAY_B)
    gray_c_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.GRAY_C)
    gray_d_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.GRAY_D)
    gray_e_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.GRAY_E)
    black_line = m.Line(m.ORIGIN, middle_col_line_width, stroke_width=35, color=m.BLACK)

    right_col = m.VGroup(
        white_line,
        gray_a_line,
        gray_b_line,
        gray_c_line,
        gray_d_line,
        gray_e_line,
        black_line
    ).arrange(m.DOWN, buff=0.4)

    right_col.next_to(gold_lines, m.DOWN, buff=0.8, aligned_edge=m.LEFT)

    all_lines = m.VGroup(
        color_lines,
        left_col,
        right_col,
    )

    blue_label = m.Text("Blue", color=m.BLUE).scale(0.5).next_to(blue_lines, m.UP, buff=0.2)
    teal_label = m.Text("Teal", color=m.TEAL).scale(0.5).next_to(teal_lines, m.UP, buff=0.2)
    green_label = m.Text("Green", color=m.GREEN).scale(0.5).next_to(green_lines, m.UP, buff=0.2)
    yellow_label = m.Text("Yellow", color=m.YELLOW).scale(0.5).next_to(yellow_lines, m.UP, buff=0.2)
    gold_label = m.Text("Gold", color=m.GOLD).scale(0.5).next_to(gold_lines, m.UP, buff=0.2)
    red_label = m.Text("Red", color=m.RED).scale(0.5).next_to(red_lines, m.UP, buff=0.2)
    maroon_label = m.Text("Maroon", color=m.MAROON).scale(0.5).next_to(maroon_lines, m.UP, buff=0.2)
    purple_label = m.Text("Purple", color=m.PURPLE).scale(0.5).next_to(purple_lines, m.UP, buff=0.2)

    color_labels = m.VGroup(
        blue_label,
        teal_label,
        green_label,
        yellow_label,
        gold_label,
        red_label,
        maroon_label,
        purple_label,
    )

    a_label = m.Text("A", color=m.BLUE).scale(0.5).next_to(blue_a_line, m.LEFT, buff=0.2)
    b_label = m.Text("B", color=m.BLUE).scale(0.5).next_to(blue_b_line, m.LEFT, buff=0.2)
    c_label = m.Text("C", color=m.BLUE).scale(0.5).next_to(blue_c_line, m.LEFT, buff=0.2)
    d_label = m.Text("D", color=m.BLUE).scale(0.5).next_to(blue_d_line, m.LEFT, buff=0.2)
    e_label = m.Text("E", color=m.BLUE).scale(0.5).next_to(blue_e_line, m.LEFT, buff=0.2)

    abc_labels = m.VGroup(
        a_label,
        b_label,
        c_label,
        d_label,
        e_label
    )

    pink_label = m.Text("Pink", color=m.BLACK).scale(0.5).move_to(pink_line)
    light_pink_label = m.Text("Light Pink", color=m.BLACK).scale(0.5).move_to(light_pink_line)
    orange_label = m.Text("Orange", color=m.BLACK).scale(0.5).move_to(orange_line)
    light_brown_label = m.Text("Light Brown", color=m.BLACK).scale(0.5).move_to(light_brown_line)
    dark_brown_label = m.Text("Dark Brown", color=m.BLACK).scale(0.5).move_to(dark_brown_line)
    gray_brown_label = m.Text("Gray Brown", color=m.BLACK).scale(0.5).move_to(gray_brown_line)

    left_col_labels = m.VGroup(
        pink_label,
        light_pink_label,
        orange_label,
        light_brown_label,
        dark_brown_label,
        gray_brown_label
    )

    white_label = m.Text("White", color=m.BLACK).scale(0.5).move_to(white_line)
    gray_a_label = m.Text("Gray A", color=m.BLACK).scale(0.5).move_to(gray_a_line)
    gray_b_label = m.Text("Gray B", color=m.BLACK).scale(0.5).move_to(gray_b_line)
    gray_c_label = m.Text("Gray C", color=m.BLACK).scale(0.5).move_to(gray_c_line)
    gray_d_label = m.Text("Gray D", color=m.BLACK).scale(0.5).move_to(gray_d_line)
    gray_e_label = m.Text("Gray E", color=m.BLACK).scale(0.5).move_to(gray_e_line)
    black_label = m.Text("Black", color=m.WHITE).scale(0.5).move_to(black_line)

    right_col_labels = m.VGroup(
        white_label,
        gray_a_label,
        gray_b_label,
        gray_c_label,
        gray_d_label,
        gray_e_label,
        black_label
    )

    preview = m.VGroup(
        all_lines,
        color_labels,
        abc_labels,
        left_col_labels,
        right_col_labels
    )
    preview.move_to(m.ORIGIN)

    return preview


