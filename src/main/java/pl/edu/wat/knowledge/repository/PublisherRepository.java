package pl.edu.wat.knowledge.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import pl.edu.wat.knowledge.entity.Publisher;

@RepositoryRestResource(collectionResourceRel = "publisher", path = "publisher")
public interface PublisherRepository extends MongoRepository<Publisher, String> {
}
