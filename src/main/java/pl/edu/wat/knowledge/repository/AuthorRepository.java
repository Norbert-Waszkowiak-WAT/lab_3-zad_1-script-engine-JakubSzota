package pl.edu.wat.knowledge.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import pl.edu.wat.knowledge.entity.Author;

@RepositoryRestResource(collectionResourceRel = "author", path = "author")
public interface AuthorRepository extends MongoRepository<Author, String> {

}
