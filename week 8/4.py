print(
    any(
        tuple(
            map(
                lambda x: x == 0, map(
                    lambda y: int(input()), range(int(input()))
                )
            )        
        )    
    )
)