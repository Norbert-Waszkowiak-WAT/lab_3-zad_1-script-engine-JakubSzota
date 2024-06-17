package pl.edu.wat.knowledge.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import pl.edu.wat.knowledge.entity.Chapter;

@RepositoryRestResource(collectionResourceRel = "chapter", path = "chapter")
public interface ChapterRepository extends MongoRepository<Chapter, String> {
}
