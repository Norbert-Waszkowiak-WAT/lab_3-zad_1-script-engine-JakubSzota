package pl.edu.wat.knowledge.entity;
 
import lombok.Data;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.MongoId;
 
import org.springframework.lang.Nullable;
import java.util.List;
 
@Data
public class Affiliation {
    @MongoId
    private String id;
    private String name;
    @Nullable
    private Affiliation parent;
}