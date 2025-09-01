book_summaries_dict = {
    "The Hobbit": (
        "Bilbo Baggins, a peaceful hobbit with no desire for adventure, is unexpectedly swept "
        "into a quest with Gandalf and thirteen dwarves to reclaim their homeland and treasure "
        "from the dragon Smaug. "
        "Along the way, Bilbo faces trolls, goblins, and giant spiders, discovering courage and "
        "cleverness he never knew he had. "
        "The story celebrates friendship, bravery, and the joy of unexpected journeys."
    ),
    "1984": (
        "George Orwell’s novel portrays a totalitarian society under absolute state control. "
        "People are constantly monitored by 'Big Brother,' and independent thought is considered a crime. "
        "Winston Smith, the protagonist, secretly rebels against this oppressive regime in search of truth "
        "and freedom. "
        "It is a chilling exploration of surveillance, propaganda, and the fragility of individual liberty."
    ),
    "To Kill a Mockingbird": (
        "Set in the racially divided American South, the novel follows Scout Finch as she grows up in the town of Maycomb. "
        "Her father, Atticus, defends a Black man falsely accused of rape, exposing Scout to harsh realities of prejudice and injustice. "
        "Through Scout’s eyes, we see the struggles of morality, compassion, and childhood innocence. "
        "The story is a powerful meditation on justice, empathy, and moral growth."
    ),
    "The Great Gatsby": (
        "F. Scott Fitzgerald’s classic captures the excesses of the Jazz Age through the eyes of Nick Carraway. "
        "He becomes entangled in the life of his mysterious neighbor, Jay Gatsby, who throws lavish parties to win back Daisy Buchanan. "
        "Behind the glamour lies obsession, illusion, and tragedy. "
        "The novel explores the corruption of the American Dream and the emptiness of material wealth."
    ),
    "Fahrenheit 451": (
        "In a dystopian future where books are outlawed, firemen are tasked with burning them. "
        "Guy Montag, a fireman, begins to question this oppressive system after encounters with a curious young woman "
        "and a group of rebels who cherish knowledge. "
        "His awakening sets him on a dangerous path toward truth and freedom. "
        "The story highlights themes of censorship, conformity, and the power of ideas."
    ),
    "The Little Prince": (
        "A poetic tale about a young prince who travels from planet to planet, meeting unusual inhabitants along the way. "
        "Through his encounters, he learns lessons about love, loneliness, and human folly. "
        "The narrator, an aviator stranded in the desert, reflects on childhood innocence and imagination. "
        "The book is both a fable for children and a profound allegory for adults."
    ),
    "Romeo and Juliet": (
        "In Verona, two young lovers from feuding families fall passionately in love. "
        "Their secret romance defies their parents’ hatred, but fate and misunderstanding lead to their tragic deaths. "
        "The story critiques the destructiveness of conflict while celebrating the intensity of youthful love. "
        "It remains one of Shakespeare’s most enduring tragedies."
    ),
    "Crime and Punishment": (
        "Rodion Raskolnikov, a poor student in St. Petersburg, murders a pawnbroker believing he can justify the act "
        "with his theory of extraordinary individuals. "
        "Consumed by guilt and paranoia, he struggles with moral dilemmas and psychological torment. "
        "The novel examines themes of justice, redemption, and the human conscience. "
        "It is both a crime story and a deep philosophical exploration."
    ),
    "Harry Potter and the Philosopher’s Stone": (
        "Harry, an orphan living with cruel relatives, discovers he is a wizard and is invited to study at Hogwarts. "
        "There, he makes close friends, learns magic, and confronts the dark legacy of Lord Voldemort. "
        "With Ron and Hermione, he solves mysteries and proves his bravery. "
        "The story blends adventure, friendship, and the discovery of destiny."
    ),
    "Don Quixote": (
        "An aging nobleman, obsessed with tales of chivalry, reinvents himself as the knight Don Quixote. "
        "Accompanied by his loyal squire Sancho Panza, he sets out on comical and misguided adventures, "
        "often mistaking windmills for giants and inns for castles. "
        "The novel satirizes medieval romances while exploring themes of illusion, reality, and the power of imagination. "
        "It is both a parody and a profound reflection on human dreams."
    ),
}


def get_summary_by_title(title: str) -> str:
    """
    Retrieve the summary for an exact book title.

    Args:
        title (str): The exact title of the book.

    Returns:
        str: The book's summary if found, otherwise a 'not found' message.
    """
    return book_summaries_dict.get(
        title,
        f"Sorry, no summary available for the title: '{title}'."
    )