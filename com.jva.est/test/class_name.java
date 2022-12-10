import com.fasterxml.jackson.annotation.JsonProperty;

public class UserDTO {
    private String id;
    private String name;
    private String email;
    public void setId(String id) {
        this.id = id;
    }
    @JsonProperty("id")
    public String getId() {
        return this.id;
    }
    public void setName(String name) {
        this.name = name;
    }
    @JsonProperty("name")
    public String getName() {
        return this.name;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    @JsonProperty("email")
    public String getEmail() {
        return this.email;
    }
}
