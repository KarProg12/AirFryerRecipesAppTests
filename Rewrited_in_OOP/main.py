import app_funcs


bulka_z_maslem = app_funcs.Recipe("Bułka z masłem", "Szybkie śniadanie", "Kup bułkę, pokrój ją i posmaruj masłem",
                   ["bułka", "masło"])
bulka_z_maslem._display_formatted()

bulka_z_dzemem = app_funcs.Recipe("Bułka z dżemem", "Drugie szybkie śniadanie",
                        "Kup bułkę i dżem (jeśli go nie masz) i posmaruj masłem a potem dżemem",
                        ["bułka", "masło", "dżem"])
bulka_z_dzemem._display_formatted()