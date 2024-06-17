package pl.edu.wat.knowledge.entity;
 
import lombok.Data;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.MongoId;
 
import org.springframework.lang.Nullable;
import java.util.List;
 
@Data
public class Book {
    @MongoId
    private String id;
    private Isbn isbn;
    private Integer year;
    private Publisher publisher;
    private Integer baseScore;
    private String title;
    @Nullable
    @DBRef
    private Author editor;
    @DBRef
    private Publisher publisher;
}