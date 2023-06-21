class Movie:
    def __init__(self, m_id, title, img, rank, summary):
        self.description = {
            "id": m_id,
            "title": title,
            "image": img,
            "rank": rank,
            "summary": summary,
        }

    def get_movie(self):
        return self.description
