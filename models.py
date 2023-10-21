# Base - declarative_base
class Views(Base):
    uid = Column(UUIDType, default=uuid4, primary_key=True)
    post_uid = Column(UUIDType, ForeignKey('post.uid'))
    owner_uid = Column(UUIDType, ForeignKey('user.uid'))
    post = relationship('Post', back_populates='views')
    owner = relationship('User', back_populates='views')
    __table_args__ = (UniqueConstraint('post_uid', 'owner_uid', name='unique'),)